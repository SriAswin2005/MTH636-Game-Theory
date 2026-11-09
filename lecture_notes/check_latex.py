import os
import re

def check_latex_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    errors = []
    
    # 1. Unmatched braces
    brace_count = 0
    for i, char in enumerate(content):
        if char == '{' and (i == 0 or content[i-1] != '\\'):
            brace_count += 1
        elif char == '}' and (i == 0 or content[i-1] != '\\'):
            brace_count -= 1
        if brace_count < 0:
            errors.append(f"Unmatched closing brace at char {i}")
            break
    if brace_count > 0:
        errors.append(f"Unmatched opening brace, count: {brace_count}")

    # 2. Unmatched environments
    begins = re.findall(r'\\begin\{([^}]+)\}', content)
    ends = re.findall(r'\\end\{([^}]+)\}', content)
    
    begin_counts = {}
    end_counts = {}
    
    for b in begins:
        begin_counts[b] = begin_counts.get(b, 0) + 1
    for e in ends:
        end_counts[e] = end_counts.get(e, 0) + 1
        
    for env in set(list(begin_counts.keys()) + list(end_counts.keys())):
        if begin_counts.get(env, 0) != end_counts.get(env, 0):
            errors.append(f"Mismatched environment: {env}. Begins: {begin_counts.get(env, 0)}, Ends: {end_counts.get(env, 0)}")

    # 3. Unmatched $ signs (heuristics)
    # Exclude \$ from count
    dollars = len(re.findall(r'(?<!\\)\$', content))
    if dollars % 2 != 0:
        errors.append(f"Odd number of unescaped $ signs: {dollars}")

    # 4. _ and ^ outside of math mode
    # This is harder to perfectly detect with regex, but we can look for _ or ^ 
    # not between $...$ or \[...\] or \(...\)
    # We will strip out math environments and then check for _ and ^
    
    text_content = content
    text_content = re.sub(r'(?<!\\)\$.*?(?<!\\)\$', '', text_content, flags=re.DOTALL)
    text_content = re.sub(r'\\\[.*?\\\]', '', text_content, flags=re.DOTALL)
    text_content = re.sub(r'\\\(.*?\\\)', '', text_content, flags=re.DOTALL)
    text_content = re.sub(r'\\begin\{equation\*?\}.*?\\end\{equation\*?\}', '', text_content, flags=re.DOTALL)
    text_content = re.sub(r'\\begin\{align\*?\}.*?\\end\{align\*?\}', '', text_content, flags=re.DOTALL)
    text_content = re.sub(r'\\begin\{cases\*?\}.*?\\end\{cases\*?\}', '', text_content, flags=re.DOTALL)
    
    # Also ignore comments
    text_content = re.sub(r'(?<!\\)%.*$', '', text_content, flags=re.MULTILINE)
    
    # Ignore specific macros that are allowed to have _ (like file paths or specific labels)
    text_content = re.sub(r'\\label\{.*?\}', '', text_content)
    text_content = re.sub(r'\\ref\{.*?\}', '', text_content)
    text_content = re.sub(r'\\includegraphics\[.*?\]\{.*?\}', '', text_content)

    invalid_chars = re.findall(r'(?<!\\)[_^]', text_content)
    if invalid_chars:
        # Give context
        lines = text_content.split('\n')
        for i, line in enumerate(lines):
            if re.search(r'(?<!\\)[_^]', line):
                errors.append(f"Possible unescaped _ or ^ outside math mode on line {i+1}: {line.strip()}")

    # 5. Unescaped & outside tabular/align/matrix
    # Strip tabular, matrix, align environments
    text_without_tabular = text_content
    for env in ['tabular', 'tabularx', 'matrix', 'pmatrix', 'bmatrix', 'vmatrix', 'Vmatrix', 'align', 'align*', 'cases']:
        text_without_tabular = re.sub(rf'\\begin{{{env}}}.*?\\end{{{env}}}', '', text_without_tabular, flags=re.DOTALL)
    
    # Any remaining unescaped &?
    invalid_amp = re.findall(r'(?<!\\)&', text_without_tabular)
    if invalid_amp:
        lines = text_without_tabular.split('\n')
        for i, line in enumerate(lines):
            if re.search(r'(?<!\\)&', line):
                errors.append(f"Possible unescaped & outside tabular/math mode on line {i+1}: {line.strip()}")
                
    if errors:
        print(f"--- {os.path.basename(filepath)} ---")
        for e in errors:
            print(f"  {e}")

if __name__ == '__main__':
    for f in os.listdir('.'):
        if f.endswith('.tex'):
            check_latex_file(f)
