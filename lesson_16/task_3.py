import xml.etree.ElementTree as ET
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def find_incoming_timing(xml_file, group_number):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for group in root.findall('group'):
            number = group.find('number')
            if number is not None and number.text == group_number:
                timing = group.find('timingExbytes/incoming')
                if timing is not None:
                    logger.info(f"Incoming timing for group {group_number}: {timing.text}")
                    return timing.text
                else:
                    logger.info(f"No 'timingExbytes/incoming' found for group {group_number}")

        logger.info(f"Group {group_number} not found in XML")


    except ET.ParseError as e:
        logger.error(f"Error parsing XML file: {e}")
    except FileNotFoundError:
        logger.error(f"File {xml_file} not found")


if __name__ == "__main__":
    find_incoming_timing("works_with_xml/groups.xml", "5")
