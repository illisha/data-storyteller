# Load important libraries 
import pandas as pd
import streamlit as st 


def app():
    """This application is created to help the user change the metadata for the uploaded file. 
    They can perform merges. Change column names and so on.  
    """

    # Load the uploaded data 
    data = pd.read_csv('data/main_data.csv')
    st.dataframe(data)

    ''' Change the information about column types
        Here the info of the column types can be changed using dropdowns.
        The page is divided into two columns using beta columns 
    '''
    st.markdown("#### Change the information about column types")
    
    # Use two column technique 
    col1, col2 = st.beta_columns(2)

    global name, type
    # Design column 1 
    name = col1.selectbox("Select Column", data.columns)
    name = name.lower()
    
    # Design column two 
    type = col2.selectbox("Select Column Type", ['numeric', 'categorical','object'])
    
    st.write("""Select your column name and the new type from the data.
                To submit all the changes, click on *Submit changes* """)

    
    if st.button("Change Column Type"): 

        # Set the value in the metadata and resave the file 
        col_metadata = pd.read_csv('data/metadata/column_type_desc.csv')
        st.dataframe(col_metadata[col_metadata['column_name'] == name])
        
        col_metadata.loc[col_metadata['column_name'] == name, 'type'] = type
        col_metadata.to_csv('data/metadata/column_type_desc.csv', index = False)

        st.write("Your changes have been made!")
        st.dataframe(col_metadata[col_metadata['column_name'] == name])