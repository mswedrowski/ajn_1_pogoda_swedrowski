import morfeusz2
import click

@click.command()
@click.option('--file',  help='Path to file.')
def main(file: str):
    morf = morfeusz2.Morfeusz()

    with open(file, 'r') as f:
        text = f.read()

    result = morf.analyse(text)
    line = []
    id = 0
    for word in result:
        if word[0] != id:
            print(", ".join(line))
            line = []
            id = word[0]

        line.append(f"{word[2][1]}:{word[2][2]}")

if __name__ == "__main__":
    main()