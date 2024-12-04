Popis:

Tento skript provádí automatické hledání optimální prahové hodnoty pro binarizaci obrázku. Skript načte šedotónový obrázek, vyzkouší všechny možné prahové hodnoty (od 0 do 255) a zjistí, která z nich vede k nejlepšímu rozdělení pixelů na bílé a černé. Optimální práh je určen na základě maximálního podílu bílých pixelů v binarizovaném obrázku.

Použití:

Upravte cestu k obrázku v proměnné image_path.
Spusťte skript v Pythonu.
Skript zobrazí dvě verze obrázku:
Původní šedotónový obrázek.
Binarizovaný obrázek s optimálním prahováním.
Skript také vypíše optimální prahovou hodnotu.

Description:

This script performs automatic threshold optimization for image binarization. It loads a grayscale image, tests all possible threshold values (from 0 to 255), and determines which one leads to the best division of pixels into white and black. The optimal threshold is selected based on the maximum proportion of white pixels in the binarized image.

Usage:

Modify the image_path variable to point to your image.
Run the script in Python.
The script will display two versions of the image:
The original grayscale image.
The binarized image with the optimal threshold.
The script will also print the optimal threshold value.
