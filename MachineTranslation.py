

class TokenizerWrap(Tokenizer):
    """Wrap the Tokenizer-class from Keras with more functionality."""
    
    def __init__(self, texts, padding,
                 reverse=False, num_words=None):
        """
        :param texts: List of strings. This is the data-set.
        :param padding: Either 'post' or 'pre' padding.
        :param reverse: Boolean whether to reverse token-lists.
        :param num_words: Max number of words to use.
        """

        Tokenizer.__init__(self, num_words=num_words)

        # Create the vocabulary from the texts.
        self.fit_on_texts(texts)

        # Create inverse lookup from integer-tokens to words.
        self.index_to_word = dict(zip(self.word_index.values(),
                                      self.word_index.keys()))

        # Convert all texts to lists of integer-tokens.
        # Note that the sequences may have different lengths.
        self.tokens = self.texts_to_sequences(texts)

        if reverse:
            # Reverse the token-sequences.
            self.tokens = [list(reversed(x)) for x in self.tokens]
        
            # Sequences that are too long should now be truncated
            # at the beginning, which corresponds to the end of
            # the original sequences.
            truncating = 'pre'
        else:
            # Sequences that are too long should be truncated
            # at the end.
            truncating = 'post'

        # The number of integer-tokens in each sequence.
        self.num_tokens = [len(x) for x in self.tokens]

        # Max number of tokens to use in all sequences.
        # We will pad / truncate all sequences to this length.
        # This is a compromise so we save a lot of memory and
        # only have to truncate maybe 5% of all the sequences.
        self.max_tokens = np.mean(self.num_tokens) \
                          + 2 * np.std(self.num_tokens)
        self.max_tokens = int(self.max_tokens)

        # Pad / truncate all token-sequences to the given length.
        # This creates a 2-dim numpy matrix that is easier to use.
        self.tokens_padded = pad_sequences(self.tokens,
                                           maxlen=self.max_tokens,
                                           padding=padding,
                                           truncating=truncating)

    def token_to_word(self, token):
        """Lookup a single word from an integer-token."""

        word = " " if token == 0 else self.index_to_word[token]
        return word 

    def tokens_to_string(self, tokens):
        """Convert a list of integer-tokens to a string."""

        # Create a list of the individual words.
        words = [self.index_to_word[token]
                 for token in tokens
                 if token != 0]
        
        # Concatenate the words to a single string
        # with space between all the words.
        text = " ".join(words)

        return text
    
    def text_to_tokens(self, text, reverse=False, padding=False):
        """
        Convert a single text-string to tokens with optional
        reversal and padding.
        """

        # Convert to tokens. Note that we assume there is only
        # a single text-string so we wrap it in a list.
        tokens = self.texts_to_sequences([text])
        tokens = np.array(tokens)

        if reverse:
            # Reverse the tokens.
            tokens = np.flip(tokens, axis=1)

            # Sequences that are too long should now be truncated
            # at the beginning, which corresponds to the end of
            # the original sequences.
            truncating = 'pre'
        else:
            # Sequences that are too long should be truncated
            # at the end.
            truncating = 'post'

        if padding:
            # Pad and truncate sequences to the given length.
            tokens = pad_sequences(tokens,
                                   maxlen=self.max_tokens,
                                   padding='pre',
                                   truncating=truncating)

        return tokens


class Machine_Translation:
  def __init__(self):
    print ('Available Languages : ') 
    print ('bg - Bulgarian')
    print ('cs - Czech')
    print ('da - Danish')
    print ('de - German')
    print ('el - Greek')
    print ('es - Spanish')
    print ('et - Estonian')
    print ('fi - Finnish')
    print ('fr - French')
    print ('hu - Hungarian')
    print ('it - Italian')
    print ('lt - Lithuanian')
    print ('lv - Latvian')
    print ('nl - Dutch')
    print ('pl - Polish')
    print ('pt - Portuguese')
    print ('ro - Romanian')
    print ('sk - Slovak')
    print ('sl - Slovene')
    print ('sv - Swedish')
    
    print ('Default Language Code : - da -> Danish')
        
    print ('---------------------------------OHH YEAH-------------------------------')
    
  
  # Setting the Language Code
  def setLanguageCode(self,language_code = 'da'):
    self.language_code = language_code
   
  
  # Download Data
  def downloaddata(self,data_dir = 'data/europarl/'):
    data_dir = data_dir
    data_url = 'http://www.statmt.org/europarl/v7/'
    print ('Fetching Data From ....................')
    print ('Url : ' + str(data_url))
    language_code = self.language_code
    url = data_url + language_code + '-en.tgz'
    print ('Calling Download and Extract Function : ')
    self.maybe_download_and_extract(url ,download_dir = data_dir)
  
  
  
  # Print Download Progress
  def _print_download_progress(self,count, block_size, total_size):
    """
    Function used for printing the download progress.
    Used as a call-back function in maybe_download_and_extract().
    """
    # Percentage completion.
    pct_complete = float(count * block_size) / total_size

    # Status-message. Note the \r which means the line should overwrite itself.
    msg = "\r- Download progress: {0:.1%}".format(pct_complete)

    # Print it.
    sys.stdout.write(msg)
    sys.stdout.flush()
    

   
  # Maybe Download and Extract
  def maybe_download_and_extract(self,url,download_dir):
    """
    Download and extract the data if it doesn't already exist.
    Assumes the url is a tar-ball file.
    :param url:
        Internet URL for the tar-file to download.
        Example: "https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz"
    :param download_dir:
        Directory where the downloaded file is saved.
        Example: "data/CIFAR-10/"
    :return:
        Nothing.
    """

    # Filename for saving the file downloaded from the internet.
    # Use the filename from the URL and add it to the download_dir.
    filename = url.split('/')[-1]
    file_path = os.path.join(download_dir, filename)

    # Check if the file already exists.
    # If it exists then we assume it has also been extracted,
    # otherwise we need to download and extract it now.
    if not os.path.exists(file_path):
        # Check if the download directory exists, otherwise create it.
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        # Download the file from the internet.
        file_path, _ = urllib.request.urlretrieve(url=url,
                                                  filename=file_path,
                                                  reporthook=self._print_download_progress)

        print()
        print("Download finished. Extracting files.")

        if file_path.endswith(".zip"):
            # Unpack the zip-file.
            zipfile.ZipFile(file=file_path, mode="r").extractall(download_dir)
        elif file_path.endswith((".tar.gz", ".tgz")):
            # Unpack the tar-ball.
            tarfile.open(name=file_path, mode="r:gz").extractall(download_dir)

        print("Done.")
    else:
        print("Data has apparently already been downloaded and unpacked.")
   
  
  
  # Load Data
  def load_data(self , english=True, start="", end="" , data_dir = 'data/europarl/'):
    """
    Load the data-file for either the English-language texts or
    for the other language (e.g. "da" for Danish).
    All lines of the data-file are returned as a list of strings.
    :param english:
      Boolean whether to load the data-file for
      English (True) or the other language (False).
    :param language_code:
      Two-char code for the other language e.g. "da" for Danish.
      See list of available codes above.
    :param start:
      Prepend each line with this text e.g. "ssss " to indicate start of line.
    :param end:
      Append each line with this text e.g. " eeee" to indicate end of line.
    :return:
      List of strings with all the lines of the data-file.
    """
    
    data_dir = data_dir
    language_code = self.language_code
    
    print ('Loading Data ---------------------------')
    
    print ('Start : ' + str(start))
    print ('--------------')
    print ('End : ' + str(end))

    if english:
        # Load the English data.
        filename = "europarl-v7.{0}-en.en".format(language_code)
    else:
        # Load the other language.
        filename = "europarl-v7.{0}-en.{0}".format(language_code)

    # Full path for the data-file.
    path = os.path.join(data_dir, filename)

    # Open and read all the contents of the data-file.
    with open(path, encoding="utf-8") as file:
        # Read the line from file, strip leading and trailing whitespace,
        # prepend the start-text and append the end-text.
        texts = [start + line.strip() + end for line in file]
        
    
    print ('Loading Successfull --------------------------------')

    return texts
  

  ## Converting text to tokens
  def Tokens(self,text,padding,reverse,num_words):
    
    print ('Text : ' + str(text))
    print ('Padding : ' + str(padding))
    print ('Reverse : ' + str(reverse))
    print ('Num_Words : ' + str(num_words))
    
    tokenizer = TokenizerWrap(texts=text,
                              padding=padding,
                              reverse=reverse,
                              num_words=num_words)
    
    return tokenizer.tokens_padded
    
  