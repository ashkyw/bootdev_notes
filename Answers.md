```python
import re

def extract_inline_segments(text):
    inline_list = []
    for block in text:
        if block == "[":
            links = extract_markdown_links(text)
            if links is not None:
                for link in links:
                    link = ("link", ) + link
                    inline_list.append(link)
        if block == "!":
            check = block
            if block == "[":
                check = check + block
                if check == "![":
                    image = extract_markdown_images(text)
                    if image is not None:
                        for item in image:
                            item = ("image", ) + item
                            inline_list.append(item)
   
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
