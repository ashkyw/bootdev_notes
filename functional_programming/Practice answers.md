CH7 - L5:
```py
def create_markdown_image(alt_text):
    new_text = f"![{alt_text}]"
    
    def create_url(url):
        clean_url = url.replace("(", "%28").replace(")", "%29")
        new_url = f"({clean_url})"
        f"{new_text}({new_url})"
        
        def create_title(title=None):
            if title is not None:
                new_title = f'"{title}"'
                url_title = clean_url.replace(")"," ")
                markdown_text = f"{new_text}({url_title} {new_title})"
                return markdown_text
            #else: return None
        return create_title
    return create_url
```

CH7 - L6:
