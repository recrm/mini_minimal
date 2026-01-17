from pathlib import Path
import shutil

from jinja2 import Environment, FileSystemLoader
import markdown

import config


ENV = Environment(loader=FileSystemLoader(config.TEMPLATE_FOLDER))


def parse_metadata(file):
    head = file.readline()
    if head == config.META_SEPERATOR:
        # Gather header data
        data = {}
        while (row := file.readline()) != config.META_SEPERATOR:
            key, value = row.decode().strip().split(":", maxsplit=1)
            data[key] = value.strip()

        # get the rest of the data
        return file.read(), data
    else:
        return head + file.read(), None


def process_file(path, site_pages):
    suffix = None

    with open(path, "rb") as f:
        content, params = parse_metadata(f)

    # Process the rest of markdown
    if path.suffix == config.MARKDOWN_SOURCE:
        content = markdown.markdown(content.decode()).encode()
        suffix = config.MARKDOWN_TARGET

    if params is not None:
        template = ENV.from_string(content.decode())
        content = template.render(page=params, site=site_pages)

        if config.TEMPLATE_ATTRIBUTE in params:
            template = ENV.get_template(params[config.TEMPLATE_ATTRIBUTE])
            content = template.render(content=content, page=params, site=site_pages)

        content = content.encode()

    return content, suffix


def process_project(root, output):
    # First, we need to delete the old output folder.
    # We need to do this to prevent caching issues.
    try:
        shutil.rmtree(str(output))
    except FileNotFoundError:
        pass

    index = len(root.parts)
    all_pages = []
    for current, folders, files in root.walk(root):

        # Collect data about all of the files.
        new_root = output.joinpath(Path(*current.parts[index:]))

        # Collect metadata about all available files.
        for file in files:
            old_path = current.joinpath(file)
            new_path = new_root.joinpath(file)

            with open(old_path, "rb") as f:
                content, params = parse_metadata(f)
            if params is None:
                params = {}

            params["path"] = str(Path(*new_path.parts[1:]))
            all_pages.append((old_path, new_path, params))

    # Now we will generate all the files.
    site_pages = [i[2] for i in all_pages]
    for old_path, new_path, params in all_pages:
        new_content, new_suffix = process_file(old_path, site_pages)

        # Write content to disk
        new_path.parent.mkdir(parents=True, exist_ok=True)
        new_path.write_bytes(new_content)
        if new_suffix:
            new_path.rename(new_path.with_suffix(new_suffix))


def main():
    process_project(Path(config.INPUT_FOLDER), Path(config.OUTPUT_FOLDER))


if __name__ == "__main__":
    main()
