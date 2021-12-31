import re


def main():
    # Read fron final_results.txt and create a new file with the results without duplicates
    with open('out/final_results.txt', 'r') as f:
        results_lines = f.readlines()
        clean_results_lines = []

        for line in results_lines:
            # get capture group for first two words in line
            # regex match letters 
            dual_type_matcher = re.match(r'(\w+),(\w+):\s(\d+)', line)
        
            if dual_type_matcher:
                regExp = re.compile(f'{dual_type_matcher.group(2)},{dual_type_matcher.group(1)}:\s(\d+)')    
                if not any(regExp.match(line) for line in clean_results_lines):
                    clean_results_lines.append(line)
                else: 
                    print('hit')
            else:
                clean_results_lines.append(line)
        
        with open('out/final_results_clean.txt', 'w') as f:
            f.writelines(clean_results_lines)


if __name__ == '__main__':
    main()