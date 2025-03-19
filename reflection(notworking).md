# Reflection

Student Name:  Katharine Batista
Sudent Email:  kebatist@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`

First to address this assignment. I thought that it was fairly simple and maybe more well explained than the past ones. Now that I know the more code you have (even if it does not work) the better the bot understands your thought process is very helpful to me. As you'll see in the unibrow file, I tested a few different methods including creating a `cols` variable within the file using the `if` statement.

I utilized Copilot when creating the `if` file statement in `unibrow.py`. While I did not think it was confusing, I used Copilot to examine the code it generated based on my writing multiple times. I learned that leveraging AI tools can significantly enhance my coding efficiency and help me understand different approaches to solving a problem. However, I still need more practice in writing proper exit conditions for loops and understanding the nuances of different loop structures. This will help me become more proficient in writing clean and efficient code.

I do not have much to about pandaslib.py but I did think that portions of the code such as 

def get_column_names(df : pd.DataFrame) -> list[str]:
    '''
    Get all column names of a pandas dataframe df
    Returns the names as a list of string
    '''
    return df.columns.tolist()

.tolist() was a term I was no familiar with but once I reallized that the term was assigned each value in the columns to the list/variable as a string. I found it interesting that there was not a special string method to identify the strings into the list. Perhaps this is a common Java practice but sometimes int, floats, and strings all have different practices when it comes to assignment to lists or input/output. 

The most confusing portion of this is the code below. 

def load_file(file_path: str, ext: str) -> pd.DataFrame:
    '''
    Load a file into a pandas dataframe assumed the file type from the extension
    return a pandas dataframe
    only suppose csv, excel and json file extensions
    - when csv assume first row is header
    - when json assume record-oriented data
    '''
    if ext == 'csv':
        return pd.read_csv(file_path)
    elif ext == 'xlsx':
        return pd.read_excel(file_path)
    elif ext == 'json':
        return pd.read_json(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")
 
This was most challenging for me becuse it utilized the file path technique but throhg working with it I was able to decipher that the file path function is there to guide the program into the function. 

As a result, file_path specifies a path that expects a string for the file that is being requsted. ext was the most confusing part of this for me but I was able to troublshoot my understandning using copiloit. Copiloto explained ext to me as somethign that is an additional string which helps determine the type of file (in this case CSV, excel). pd.DataFrame, which indicates that it will return a DataFrame object from the pandas library. After all of this, I learned that this specific program reads and laods the content of the file into its pandas dataframe that is being built in the variale portion of the function. Additionally, dataFrames are a common data structure that is often used for Python analysis and data maniuplation. Similar to this situation.