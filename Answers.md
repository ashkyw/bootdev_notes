```python
import re

def extract_inline_segments(text):
    inline_list = []
    split_text = text.split()
    for block in split_text:
        if block.startswith("!["):
            image = extract_markdown_images(block)
            if image is not None:
                for item in image:
                    item = ("image", ) + item
                    inline_list.append(item)            
        if block.startswith("["):
            links = extract_markdown_links(block)
            if links is not None:
                for link in links:
                    link = ("link", ) + link
                    inline_list.append(link)

    return inline_list


def extract_markdown_images(text):
    image_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    image_matches = re.findall(image_pattern, text)
    return image_matches


def extract_markdown_links(text):
    link_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    link_matches = re.findall(link_pattern, text)
    return link_matches
```
