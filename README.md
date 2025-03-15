
# Shayar AI - Generate Ghazals with Artificial Intelligence

Shayar AI is an innovative project that generates entire ghazals based on a single input word, utilizing advanced machine learning models like LSTM, GRU, and RNN. The project aims to automate the process of creating poetic couplets (shairi) in Roman Urdu, offering a creative and fun way to experience traditional Urdu poetry. The system also converts generated text into speech using Play.ht.

## Features
- **Ghazal Generation**: Generate beautiful ghazals from a single word input using AI-driven models.
- **Speech Synthesis**: Converts generated poetry into speech using Play.ht for an interactive experience.
- **Roman Urdu Support**: Specifically designed to work with Roman Urdu for a wider audience.
- **Customizable Inputs**: Allows users to input any word to generate personalized poetry.

## Technologies Used
- **LSTM / GRU / RNN**: Machine learning models for generating poetry.
- **Play.ht**: Converts the generated text into speech for better accessibility and interaction.
- **Python**: The primary language for model training and data processing.
- **TensorFlow/Keras**: For deep learning model implementation.
- **BeautifulSoup**: For scraping poetry data from Rekhta.org.

## Getting Started
To get started with Shayar AI, clone the repository and follow the steps below:

### Prerequisites
- [Python 3.8+](https://www.python.org/)
- [TensorFlow](https://www.tensorflow.org/)
- [Play.ht API Key](https://play.ht/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/sufyanbinimran/Generative-AI.git
    ```

2. Navigate to the project folder:
    ```bash
    cd Generative-AI
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the poetry generation script:
    ```bash
    python generate_poetry.py
    ```

5. To hear the generated poetry, use the integrated Play.ht API.

## Contributing
We encourage contributions to make Shayar AI even better. Feel free to fork the repository, submit issues, and create pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


For more details or support, visit the [GitHub Repository](https://github.com/sufyanbinimran/Generative-AI).
