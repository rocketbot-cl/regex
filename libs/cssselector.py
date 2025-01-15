def xpath_to_css(xpath):
        
        if not xpath:
                raise Exception('Xpath undefined')

        css_parts = []
        parts = xpath.split("/")

        for part in parts:
            
            if not part or part == "":
                continue

            # Selector de id
            if "@id=" in part:
                id_name = part.split('="')[1].split('"')[0]
                css_parts.append(f"#{id_name}")

            # Selector de clase
            elif "contains(@class," in part:
                class_name = part.split('="')[1].split('"')[0]
                css_parts.append(f".{class_name}")

            # Selector de nth-child
            elif "[" in part and "]" in part:
                tag_name, child_num = part.split("[")
                child_num = child_num.strip("]")
                css_parts.append(f"{tag_name}:nth-child({child_num})")

            # Selector de tag
            else:
                css_parts.append(part)

        # Unir las partes para formar el selector CSS completo
        css = " > ".join(css_parts)
        print(css)
        return css

xpath = "/html/body/form/fieldset[2]/label[2]"
css_selector = xpath_to_css(xpath)


def main(selector):
    # Verifica si el selector es un XPath
        if selector.startswith('//') or selector.startswith('/'):
            # si es un XPath, lo convierte a CSS selector
            css_selector = xpath_to_css(selector)
            print(f"El selector original era un XPath: {selector}")
            print(f"El selector convertido a CSS selector es: {css_selector}")

selector = input("Ingresa un selector (XPath o CSS): ")
main(selector)