class FileAnalyzer:
    def __init__(self, filename):
        self._filename = filename
        with open(filename, 'r') as f:
            self._content = f.read()
            for c in ".@:()_=#[]":
                self._content = self._content.replace(c, ' ')

    def display_content(self):
        return self._content

    def number_of_words(self):
        return len(self._content.split())

    def display_with_line_number(self):
        return '\n'.join(f'{idx + 1}.   {val}' for idx, val in enumerate(self._content.split('\n')))

    def search(self, word):
        lines = []
        for idx, val in enumerate(self._content.split('\n')):
            if word in val:
                lines.append(idx + 1)

        return lines

    def append_a_line(self, line):
        self._content += line + '\n'

if __name__ == '__main__':
    f1 = FileAnalyzer('lab1-6.py')
    print(f1.display_content())
    print('\n')
    print(f1.number_of_words())
    print('\n')
    print(f1.display_with_line_number())
    print('\n')
    print(f1.search('def'))
    f1.append_a_line('# Happy OOP')
    print(f1.display_content())
    print(f1.display_with_line_number())
