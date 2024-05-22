from markdown_pdf import MarkdownPdf,Section
import markdown

def generate_cv_files():
    pdf = MarkdownPdf(toc_level=2)
    with open("./CV.md") as f:
        lines_joined = ""
        for line in f:
            lines_joined += f"{line}\n"
        pdf.add_section(Section(
            lines_joined,
            toc=False
        ))
    pdf.meta["title"] = "Sam Bowman - DevOps Engineer - CV"
    pdf.meta["author"] = "Sam Bowman"
    pdf.save("./static/files/CV.pdf")

    with open("./CV.md") as f:
        md = f.read()

    html = markdown.markdown(md)

    with open("./templates/cv_content.html", 'w') as f:
        f.write(html)

if __name__ == "__main__":
    generate_cv_files()