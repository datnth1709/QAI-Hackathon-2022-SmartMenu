# STEP 1: Pull python image
FROM python:3.7

# STEP 2,3: CREATE WORK DIR AND COPY FILE TO WORK DIR
WORKDIR /khoinlg_menu
COPY requirements.txt /khoinlg_menu

# STEP 4,5,6: INSTALL NECESSARY PACKAGE
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gdown

# STEP 7: Download file weight if needed
# RUN gdown "https://drive.google.com/uc?export=download&id=1VIplhJoaKPI08Qcdq6FhPk_dMvGOfDMp"

# STEP 8: RUN COMMAND
COPY . /khoinlg_menu
CMD ["python", "./api.py"]
