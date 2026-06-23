import re
import glob
import os

def increase_size(match):
    val_str = match.group(1)
    unit = match.group(2)
    
    if val_str.startswith('clamp') or val_str.startswith('calc'):
        return match.group(0)
        
    try:
        val = float(val_str)
    except ValueError:
        return match.group(0)
        
    if unit == 'px':
        if val < 24: # Not big
            new_val = val + 2
            if val.is_integer():
                return f"font-size: {int(new_val)}px;"
            else:
                return f"font-size: {new_val}px;"
    elif unit == 'rem' or unit == 'em':
        if val < 1.5:
            new_val = val + 0.15
            # Return up to 3 decimal places
            return f"font-size: {round(new_val, 3)}{unit};"
            
    return match.group(0)

def process_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    pattern = re.compile(r'font-size:\s*([0-9.]+)(px|rem|em);')
    new_content = pattern.sub(increase_size, content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")

def main():
    files = glob.glob('*.css') + glob.glob('*.html')
    for file in files:
        process_file(file)

if __name__ == '__main__':
    main()
