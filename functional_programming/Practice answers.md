# CH7 - L5:
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

# CH7 - L6:

```py
def new_resizer(max_width, max_height):
    
    def check_resolution(min_width=0, min_height=0):
        if min_width > max_width:
            raise Exception("minimum size cannot exceed maximum size")
        if min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")
        
        def reduce_resolution(width, height):
            if width > max_width:
                new_width = min(width, max_width)
            elif width < min_width: 
                new_width = max(width, min_width)
            else: new_width = width
            if height > max_height:
                new_height = min(height, max_height)
            elif height < min_height: 
                new_height = max(height, min_height)
            else: new_height = height
            return new_width, new_height
        
        return reduce_resolution
    
    return check_resolution
```
