from transformers import pipeline
from transformers import BartTokenizer, BartForConditionalGeneration
import logging
import termcolor
import torch


def print_green(text):
    print(termcolor.colored(text, "green"))


class Summarizer:
    """Helper class for summarizing text using BART"""

    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
        self.model = BartForConditionalGeneration.from_pretrained(
            "facebook/bart-large-cnn"
        )
        logging.info("Summarizer initialized")

    def summarize(self, text: str):
        """Create a summary of the input text using BART"""
        print_green(f"Summarizing ")
        inputs = self.tokenizer(
            [text], return_tensors="pt", max_length=1024, truncation=True
        )
        summary_ids = self.model.generate(
            inputs["input_ids"], num_beams=2, max_length=100, early_stopping=True
        )
        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
