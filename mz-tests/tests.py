from klpt.preprocess import Preprocess
from klpt.tokenize import Tokenize

def read_text(file_path: str) -> list[str]:
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        return file.read().split(" ")


def main(kurdish_words: list[str]) -> None:
    """
    First let's just test if we can bring their code to test
    okk
    """
    
    # this creates a preprocessor for Sorani Kurdish written in Arabic script
    preprocessor_ckb = Preprocess("Sorani", "Arabic", numeral="Latin")
    tokenizer_ckb = Tokenize("Sorani", "Arabic")

    for word in kurdish_words:
        preprocessed_word = preprocessor_ckb.preprocess(word)
        tokenized_word = tokenizer_ckb.word_tokenize(word)
        print(f"Original: {word} | Preprocessed: {preprocessed_word} | Tokenized: {tokenized_word}")

    


if __name__ == "__main__":
    text_file = read_text("tests.txt")
    main(text_file)