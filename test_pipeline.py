from src.textSummarizer.pipeline.prediction_pipeline import PredictionPipeline

if __name__ == "__main__":
    text = "Artificial Intelligence is transforming industries and making human life more efficient."
    summarizer = PredictionPipeline()
    summary = summarizer.predict(text)
    print("Summary:", summary)
