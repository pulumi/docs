const EU_COUNTRY_CODES: Record<string, string> = {
    BE: "Belgium", EL: "Greece", LT: "Lithuania", PT: "Portugal",
    BG: "Bulgaria", ES: "Spain", LU: "Luxembourg", RO: "Romania",
    CZ: "Czech Republic", FR: "France", RE: "Reunion", GP: "Guadeloupe",
    MQ: "Martinique", GF: "French Guiana", YT: "Mayotte", BL: "Saint Barthelemy",
    MF: "Saint Martin", PM: "Saint Pierre and Miquelon", WF: "Wallis and Futuna",
    PF: "French Polynesia", NC: "New Caledonia", HU: "Hungary", SI: "Slovenia",
    DK: "Denmark", FO: "Faroe Islands", GL: "Greenland", HR: "Croatia",
    MT: "Malta", SK: "Slovakia", DE: "Germany", IT: "Italy",
    NL: "Netherlands", AW: "Aruba", CW: "Curacao", SX: "Sint Maarten",
    FI: "Finland", AX: "Aland Islands", EE: "Estonia", CY: "Cyprus",
    AT: "Austria", SE: "Sweden", IE: "Ireland", LV: "Latvia",
    PL: "Poland", UK: "United Kingdom", GB: "United Kingdom",
    AI: "Anguilla", BM: "Bermuda", IO: "British Indian Ocean Territory",
    VG: "British Virgin Islands", KY: "Cayman Islands", FK: "Falkland Islands",
    GI: "Gibraltar", MS: "Montserrat",
    PN: "Pitcairn, Henderson, Ducie and Oeno Islands",
    SH: "Saint Helena, Ascension and Tristan da Cunha",
    TC: "Turks and Caicos Islands", GG: "Guernsey", JE: "Jersey", IM: "Isle of Man",
};

function isInEUTimezone(): boolean {
    try {
        const tz = Intl.DateTimeFormat().resolvedOptions().timeZone;
        if (!tz) return false;
        if (tz.indexOf("Europe") >= 0) return true;
        const EU_NON_EUROPE_TIMEZONES = ["Atlantic/Canary", "Africa/Ceuta", "Atlantic/Madeira"];
        return EU_NON_EUROPE_TIMEZONES.indexOf(tz) >= 0;
    } catch {
        return false;
    }
}

function isEULocale(): boolean {
    const locale =
        (navigator.languages && navigator.languages.length > 0 && navigator.languages[0]) ||
        (navigator as any).userLanguage ||
        navigator.language;
    if (!locale) return false;
    let country = locale;
    if (locale.indexOf("-") >= 0) {
        country = locale.split("-")[1];
    }
    return !!EU_COUNTRY_CODES[country.toUpperCase()];
}

export function inEU(): boolean {
    return isInEUTimezone() || isEULocale();
}
