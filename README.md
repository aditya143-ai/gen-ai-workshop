#  Jupyter Notebook Setup Guide for VS Code (GenAI Workshop)

Welcome to the workshop! In this guide, we will walk you through setting up VS Code IDE and installing the necessary extensions to work with Jupyter notebooks. The process is detailed for both MacOS and Windows operating systems. Please follow the instructions carefully.

## Pre reads

### Mandatory reads for the session

#### 1. [Python 101](https://learnxinyminutes.com/docs/python)

#### 2. [Prompt Engineering for Engineers - on Marcel](https://learningmanagereu.adobe.com/app/learner?accountId=652#/course/1692950)

#### 3. [What is generative AI?](https://searchengineland.com/what-is-generative-ai-how-it-works-432402)


### Mandatory Deeplearning.ai trainings (DeepLearning.AI is a hands on educational platform for AI)

#### 1. [Langchain intro - Building LLM apps](https://learn.deeplearning.ai/courses/build-llm-apps-with-langchain-js/lesson/vchyb/introduction?courseName=build-llm-apps-with-langchain-js)

#### 2. [Langchain intro - Chat with your data](https://learn.deeplearning.ai/courses/langchain-chat-with-your-data/lesson/snupv/introduction?courseName=langchain-chat-with-your-data)

#### 3. [Knoweldge Graph using RAG](https://learn.deeplearning.ai/courses/knowledge-graphs-rag/lesson/mltr8/introduction?courseName=knowledge-graphs-rag)

#### 4. [Crew.ai intro - Multi agent AI systems with Crew.ai](https://learn.deeplearning.ai/courses/multi-ai-agent-systems-with-crewai/lesson/wwou5/introduction?courseName=multi-ai-agent-systems-with-crewai)

#### 5. [Crew.ai advanced - Practial use cases ](https://learn.deeplearning.ai/courses/practical-multi-ai-agents-and-advanced-use-cases-with-crewai/lesson/agfnp/introduction?courseName=practical-multi-ai-agents-and-advanced-use-cases-with-crewai)

#### 6. [Evaluating agents](https://learn.deeplearning.ai/courses/evaluating-ai-agents/lesson/pag5y/lab-1:-building-your-agent)

#### 7. [Long term memory with agents](https://learn.deeplearning.ai/courses/long-term-agentic-memory-with-langgraph/lesson/ovv0p/introduction?courseName=long-term-agentic-memory-with-langgraph)

#### 8. [Safe and reliable AI with guardrails](https://learn.deeplearning.ai/courses/safe-and-reliable-ai-via-guardrails/lesson/rz5a6/introduction?courseName=safe-and-reliable-ai-via-guardrails)

#### 9. [Model Context Protocol (MCP) to connect with external data sources and tools.](https://www.youtube.com/watch?v=5xqFjh56AwM), [Code repo](https://github.com/daveebbelaar/ai-cookbook/tree/main/mcp/crash-course)

###### _These subtopics are optional_ - `How large language models are built` _and_ `How does a transformer predict text?`
### Recommended reads for the session

#### 1. [Brief about Deep Learning](https://towardsdatascience.com/simply-deep-learning-an-effortless-introduction-45591a1c4abb)

#### 2. [Langchain quick start](https://python.langchain.com/docs/get_started/quickstart)

#### 3. [A brief about embeddings](https://towardsdatascience.com/what-is-embedding-and-what-can-you-do-with-it-61ba7c05efd8)

#### 3. [RAG techniques](https://www.analyticsvidhya.com/blog/2023/09/retrieval-augmented-generation-rag-in-ai/)

#### 5. [LLM fine tuning example](https://www.datacamp.com/tutorial/fine-tuning-llama-2)

## Prerequisites

Before you begin, make sure that you have the following:

- A working internet connection.
- A computer running either **MacOS** or **Windows**.
- **VS Code IDE** (Visual Studio Code) installed on your computer.
- **Python 3.x** installed (if not, we will guide you through this in the next steps).
- **Miniconda** setup on your machine.

If you already have **VS Code**, **Python** and **miniconda** installed, you can skip ahead to the section where we install the necessary extensions.

**Alternatively, if you are using Github CodeSpace you can skip all steps below, ensure the python environment is set via conda (you will see the option when you run) using python 3.11.x**
---

## Step 1: Install Prerequisites

### Hardware Requirements

- **CPU**: Intel Broadwell or later, or an equivalent AMD processor.
- **RAM**: At least 8GB of RAM.
- **Disk Space**: Minimum of 200GB of free disk space.
- **GPU (optional but recommended for AI tasks)**: NVIDIA GPU with CUDA support.

### Software Requirements

- **Operating Systems**:
  - Windows 10 or later
  - macOS 10.15 (Catalina) or later
  - Linux (Ubuntu 18.04 or later, CentOS 7 or later)
- **Python**: Python >=3.10 <=3.12.10(Prefferred) .


### 1. Install Python
1. Open Lion Store
2. Search for Python.
3. Run the installer once the download is complete.

### 2. Install Git (optional, but useful):
1. Open Lion Store 
2. Search for Git or [Download GIT from direct website](https://git-scm.com/download/win)
3. Run the installer once the download is complete.

### 3. Install VS Code
#### For **Windows**:
1. Go to the [VS Code download page](https://code.visualstudio.com/download).
2. Click on the **Stable** download button for **Windows** (64-bit).
3. Run the installer once the download is complete and follow the on-screen instructions.
4. Ensure that the option to **Add to PATH** is checked during installation (this will make VS Code easier to launch).

#### For **MacOS**:

1. Go to the [VS Code download page](https://code.visualstudio.com/download).
2. Click on the **Stable** download button for **Mac**.
3. Once the `.zip` file is downloaded, extract it.
4. Drag and drop the extracted **VS Code** app into your **Applications** folder.

### Only For **MacOS**:
#### Install Homebrew (if not already installed):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### Install Git (optional) if previous step not completed:
```bash
brew install git
```
---

### 4. Clone code from git repository to local machine
Create a local working folder and then in that clone the git repository
git clone https://pscode.lioncloud.net/ai-workspace/gen-ai-workshop-notebooks.git

If you have not setup your credentials yet for git then setup a Personal Access Token using the steps from https://docs.gitlab.com/user/profile/personal_access_tokens/
Once pat is setup then run the below command 
git clone https://<userid>:<pat>@pscode.lioncloud.net/ai-workspace/gen-ai-workshop-notebooks.git
e.g. git clone https://adigandh:xk3ytZL-DUMMYPAT-123@pscode.lioncloud.net/ai-workspace/gen-ai-workshop-notebooks.git

## Step 2: Install **pipx** to Avoid Dependency Conflicts
Using pipx ensures each tool runs in its own isolated environment.

#### Install  **pipx**:

1. Open the **Terminal** app.
2. Type the following command and press **Enter**:
```bash
   python3 --version
```
```bash
   python -m pip install --user pipx
```

```bash
   python -m pipx ensurepath
```
**Restart the terminal after installation.**

## Step 3: Setup a Virtual Environment for Workshop
***This ensures everyone works in the same clean Python environment.***

1. **Move Focus to respective directory**
Choose  `gen-ai-workshop-notebooks` in terminal if already not in given root directory

```bash
cd gen-ai-workshop-notebooks
```
2. **Set Up Virtual Environment**:
```bash
python -m venv genai-venv
```
3. **Activate the virtual environment:**
- On Windows:
   ```bash
   genai-venv\Scripts\activate

   ```
- On macOS:
   ```bash
  source genai-venv/bin/activate
   ```
**4. Install essential packages (can be adjusted per your workshop):**

This allows your virtual environment to be used as a Jupyter kernel.

   ```bash
  python -m pip install --upgrade pip
  python -m pip install ipykernel
  pip install -r ./requirements.txt
   ```

Then register it:
   ```bash
   python -m ipykernel install --user --name=genai-venv --display-name "Python3.11 (genai-venv)"
   ```

### Restart VS Code and Select Kernel
1. Open your .ipynb file in VS Code
2. Click the kernel name in the top right (or use Cmd/Ctrl + Shift + P → Select Kernel)
3. Choose: Python (genai-venv)
4. update .env file for respective model which you wish to use like OpenAI or AzureOpen AI

   if you are using OpenAI then update 
   ```
   OPENAI_API_KEY="your key"
   ```
   if you are using AzureOpenAI mode then update
   ```
   OPENAI_API_VERSION=2024-02-15-preview
   DEPLOYMENT_NAME=gpt-4o
   AZURE_ENDPOINT=https://test-gpt-us-region.openai.azure.com
   AZURE_API_KEY=
   ```

## Setup validations

### Resolve "Invalid Python Interpreter in VS Code" issue while running any .ipynb or vs code

```An Invalid Python interpreter is selected, please try changing it to enable features such as IntelliSense, linting, and debugging. See output for more details regarding why the interpreter is invalid.```

1. Open the Folder in VS Code *(Select which notebook you are trying to use)*:
    
   **Open the project folder in VS Code where your virtual environment (venv) exists:**
    ``` 
        rag-retrieval-augmented-generation/
                     └── venv/
    ```

2. Step 2: Open Command Palette

    **Press:**
    - Ctrl+Shift+P (Windows)
    - Cmd+Shift+P (macOS)
    
   Then search and select:

    ``Python: Select Interpreter``

3. Select the Correct Interpreter

    You should see a list of Python interpreters, including something like:
    - .venv\Scripts\python.exe (Windows)
    - ./venv/bin/python (macOS/Linux)
    
    Select the one that matches your local virtual environment.

   **If you don't see it:**
          
    Click “Enter interpreter path”  Then “Find...” and manually browse to:
   - Windows: genai-workshop\venv\Scripts\python.exe 
   - macOS/Linux: genai-workshop/venv/bin/python

4. Restart the VS code
5. Open a new terminal in VS Code:
    ```bash
    where python   # Windows
    ```
    ```bash
    which python   # macOS/Linux
    ```
   
#### Optional: Remove Unwanted Kernel Names (if too many show up)
#### You can clean up old ones:
```bash
jupyter kernelspec list
```

#### To remove one:
```bash
jupyter kernelspec uninstall <kernel_name>
```


#### Optional: Setup Ollama to run LLMs locally on your machine
https://ollama.com/
