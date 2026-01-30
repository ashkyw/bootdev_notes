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

# CH8 - L1:

```py
def file_type_aggregator(func_to_decorate):
    # dict of file_type -> count
    counts = {}

    def wrapper(doc, file_type):
        if file_type not in counts:
            counts[file_type] = 0
        counts[file_type] += 1
        result = func_to_decorate(doc, file_type)

        return result, counts

    return wrapper

@file_type_aggregator
def process_doc(doc, file_type):
    return f"Processing doc: '{doc}'. File Type: {file_type}"
```

# CH8 - L2:

```py
def args_logger(*args, **kwargs):
    n = 0
    sort_kwargs = sorted(kwargs)
    for item in args:
        n += 1
        print(f"{n}. {item}")

    for kw in sort_kwargs:
        print(f"* {kw}: {kwargs[kw]}")
```
