import pandas as pd 
import streamlit as st

def loadWishlist():
    if 'wishlist' not in st.session_state:
        st.session_state.wishlist= []

def addItem(item,link):
    st.session_state.wishlist.append({'item':item,'link':link})

def removeElement(index):
    if 0<= index < len(st.session_state.wishlist):
        st.session_state.pop(index)
        
def main():
    st.title("My Summer fashion wishlist (fullfilment estimate - May 2025)  ")
    loadWishlist();

    item=st.text_input("Enter name  - ")
    url=st.text_input("Insert Link - ")

    if item:
        addItem(item,url)
        st.success("Item is in the wishlist")
    else:
        st.warning("Please enter item name")

    if st.session_state.wishlist:
        st.subheader("Wishlist")
        df=pd.DataFrame(st.session_state.wishlist)
        st.table(df)

    delItem=st.number_input("Enter item number to remove",min_value=0,max_value=len(st.session_state.wishlist)-1,step=1)
    if st.button("Remove selected item"):
        removeElement(delItem)
        st.success("Item finally bought! Good Job Bro!!!!")
    else:
        st.info("Wishilist is emplt dog!")

if __name__ == "__main__":
    main()



