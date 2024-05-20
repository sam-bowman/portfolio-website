from flask import Flask, url_for
import pyvibe as pv

def get_navbar(title=None):
    navbar = pv.Navbar(title="Sam Bowman",logo="https://avatars.githubusercontent.com/u/64836476?v=4")
    if title:
        navbar.title = f"{title} - Sam Bowman"
    github_link=pv.NavbarlinkComponent("GitHub","https://github.com/sam-bowman")
    navbar.add_component(github_link)
    return navbar

def get_sidebar():
    # Create sidebar
    sidebar = pv.Sidebar()

    # Create sidebar categories
    sidebar_category_main = pv.SidebarcategoryComponent(title="Main")

    # Create sidebar links & attach to category - main
    sidebar_main_link_home = pv.SidebarlinkComponent(title="Home",url=url_for("index"))
    sidebar_category_main.add_component(sidebar_main_link_home)

    # Add sidebar categories to sidebar
    sidebar.add_component(sidebar_category_main)

    return(sidebar)