# Rewriting the same project using Object-Oriented Programming

class ImageProcessor:
    def __init__(self, image_size=(8, 8), brightness_increment=50):
        self.image_size = image_size
        self.brightness_increment = brightness_increment
        self.image = self._generate_image()
        self.bright_image = None
        self.edge_image = None
        self.fft_spectrum = None

    def _generate_image(self):
        """Simulates a grayscale image."""
        return np.random.randint(0, 256, self.image_size)

    def adjust_brightness(self):
        """Adjusts the brightness of the image using broadcasting."""
        self.bright_image = np.clip(self.image + self.brightness_increment, 0, 255)

    def apply_edge_detection(self, kernel=None):
        """Applies edge detection using convolution and a specified kernel."""
        if kernel is None:
            kernel = np.array([[-1, 0, 1],
                               [-2, 0, 2],
                               [-1, 0, 1]])
        img = self.image
        output = np.zeros((img.shape[0] - 2, img.shape[1] - 2))
        for i in range(output.shape[0]):
            for j in range(output.shape[1]):
                region = img[i:i+3, j:j+3]
                output[i, j] = np.sum(region * kernel)
        self.edge_image = output

    def compute_fft(self):
        """Computes FFT and its magnitude spectrum."""
        fft_result = np.fft.fft2(self.image)
        self.fft_spectrum = np.abs(fft_result)

    def run_all(self):
        """Executes all processing steps."""
        self.adjust_brightness()
        self.apply_edge_detection()
        self.compute_fft()

    def generate_report(self, pdf_path="/mnt/data/Day2_Numpy_Project_OOP.pdf"):
        """Generates a PDF report of all visuals and steps."""
        with PdfPages(pdf_path) as pdf:
            fig, ax = plt.subplots(figsize=(8.27, 11.69))
            ax.axis('off')
            text = (
                "Industry-Level Day 2 Project using OOP (Image Processing with NumPy)\n\n"
                "Class: ImageProcessor\n"
                "Methods:\n"
                "- _generate_image: Simulates a grayscale image\n"
                "- adjust_brightness: Applies brightness increment\n"
                "- apply_edge_detection: Uses Sobel filter for edge detection\n"
                "- compute_fft: Computes frequency spectrum\n"
                "- run_all: Calls all processing functions\n"
                "- generate_report: Exports results as PDF\n\n"
                "This approach promotes modularity and reusability.\n"
            )
            ax.text(0.05, 0.95, text, va='top', fontsize=12)
            pdf.savefig(fig)
            plt.close()

            fig, axs = plt.subplots(2, 2, figsize=(8.27, 11.69))
            axs[0, 0].imshow(self.image, cmap='gray')
            axs[0, 0].set_title("Original Image")
            axs[0, 0].axis('off')

            axs[0, 1].imshow(self.bright_image, cmap='gray')
            axs[0, 1].set_title("Brightened Image")
            axs[0, 1].axis('off')

            axs[1, 0].imshow(self.edge_image, cmap='gray')
            axs[1, 0].set_title("Edge Detection (Sobel)")
            axs[1, 0].axis('off')

            axs[1, 1].imshow(np.log1p(self.fft_spectrum), cmap='viridis')
            axs[1, 1].set_title("FFT Magnitude Spectrum")
            axs[1, 1].axis('off')

            plt.tight_layout()
            pdf.savefig(fig)
            plt.close()

        return pdf_path

# Run the project with OOP
processor = ImageProcessor()
processor.run_all()
oop_pdf_path = processor.generate_report()
oop_pdf_path
