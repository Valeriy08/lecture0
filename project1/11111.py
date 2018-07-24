from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os


import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "KlTblueYUb9Y3vAguZWw", "isbns": "9781632168146"})
print(res.json())
