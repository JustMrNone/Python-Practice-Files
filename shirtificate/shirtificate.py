from fpdf import FPDF

class Shirt:

    def __init__(self, name):
        self.name = name
        self.tailor()

    @classmethod
    def get(cls):
        name = input("Full name: ").strip()
        return cls(name)

    def tailor(self):
        pdf = FPDF(orientation="portrait", format="A4")
        pdf.add_page()
        pdf.set_auto_page_break(auto=False, margin=0)

        pdf.set_font("helvetica", "B", size=46)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 50, border=0, align="C", txt="CS50 Shirtificate")
        pdf.ln()

        pdf.image(
            "shirtificate.png",
            x=15,
            y=(297 / 4),
            w=180,
        )

        pdf.set_font("helvetica", "B", size=28)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(0, 150, border=0, align="C", txt=f"{self.name} took CS50")

        pdf.output("shirtificate.pdf")


def main():
    Shirt.get()

if __name__ == "__main__":
    main()
