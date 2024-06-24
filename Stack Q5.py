def match_tags(html):
    stack = []
    i = 0
    
    while i < len(html):
        if html[i] == '<':
            i += 1
            tag = ""
            
            while i < len(html) and html[i] != '>':
                tag += html[i]
                i += 1
            
            if tag.startswith('/'):
                if stack:
                    if stack[-1] == tag[1:]:
                        stack.pop()
                    else:
                        return False  # Mismatched closing tag
                else:
                    return False  # Closing tag with empty stack
            else:
                stack.append(tag)
        
        i += 1
    
    return len(stack) == 0  # Stack should be empty at the end if all tags are matched

# Example HTML content
html_content = "<html><body><h1>Hello</h1><p>World</p></body></html>"

if match_tags(html_content):
    print("Tags are properly matched!")
else:
    print("Tags are not properly matched.")