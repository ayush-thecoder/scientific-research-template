# Setup Tutorial

Welcome to your scientific research template. Follow these steps to get started:

## 1. Extract the Repo
Unzip the folder and navigate into it:
```bash
unzip scientific-research-template.zip
cd scientific-research-template
```

## 2. Create the Conda Environment
Ensure you have Conda installed, then run:
```bash
conda env create -f environment.yml
conda activate sci-env
```

## 3. Run the Example Code
```bash
make run
```
This will generate a sample plot in `figures/`.

## 4. Generate Your Paper
```bash
make paper
```

## 5. Clean the Workspace
```bash
make clean
```

## 6. Push to GitHub (Optional)
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-repo-url>
git push -u origin main
```
