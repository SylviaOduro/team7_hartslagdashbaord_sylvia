#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 21 12:17:59 2025

@author: oduro
"""
import streamlit as st
import pandas as pd


st.title("Raad het aantal snoepjes in de pot!")

st.write(f'Hi, {st.session_state["name"]} vul hieronder jouw gok in als getal (bijvoorbeeld: 57)')

# Initialiseer als nog niet aanwezig
if "gokken" not in st.session_state:
    st.session_state.gokken = []

# Tekstveld voor invoer
gok_input = st.text_input("Jouw gok:")

# Knop om in te sturen
if st.button("Verzend je gok"):
    if gok_input.isdigit():
        st.session_state.gokken.append(int(gok_input))
        st.success("Je gok is opgeslagen!")
    else:
        st.error("Vul alsjeblieft een **getal** in (bijvoorbeeld: 42)")

# Aantal deelnemers
st.subheader("Aantal deelnemers:")
st.write(len(st.session_state.gokken))

# Gegokte waardes
st.subheader("Gegokte waardes tot nu toe:")
if st.session_state.gokken:
    df = pd.DataFrame(st.session_state.gokken, columns=["Gok"])
    st.dataframe(df)
else:
    st.write("Nog geen gokken ingevuld.")
