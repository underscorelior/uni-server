import re
import tldextract


def acronym(name: str) -> str:
    common = {"of", "the", "and", "at", "for", "in", "on"}
    words = re.sub(r"[-(),]", " ", name).split()
    parts = []
    for w in words:
        if not w:
            continue
        if w.isupper() and len(w) > 1:
            parts.append(w)
        elif w.lower() not in common:
            parts.append(w[0].upper())
    return "".join(parts)


def system_acronym(name: str, system_name: str) -> str:
    system_name = system_name.strip()
    if system_name.lower() in name.lower():
        return (
            acronym(system_name) + " " + acronym(name.replace(system_name, "").strip())
        )
    if acronym(system_name).lower() in name.lower():
        return (
            acronym(system_name)
            + " "
            + acronym(name.replace(acronym(system_name), "").strip())
        )
    return None


def url_alias(name: str) -> str:
    extracted = tldextract.extract(name)
    domain = extracted.domain
    if domain.endswith(".edu"):
        domain = domain[:-4]
    return domain.upper()


def aliases(name: str, system_name: str, url: str) -> str:
    out = [acronym(name)]
    if system_name and system_acronym(name, system_name):
        out.append(system_acronym(name, system_name))
    if url_alias(url) and url_alias(url) not in out:
        out.append(url_alias(url))
    return out
