// ASCII art taglines generated with figlet (small font)
const taglineArts: string[] = [
    `           _            _
 _ __ _  _| |_  _ _ __ (_)  _  _ _ __
| '_ \\ || | | || | '  \\| | | || | '_ \\
| .__/\\_,_|_|\\_,_|_|_|_|_|  \\_,_| .__/
|_|                             |_|`,

    ` ___      _ _    _     ___           _              __  __
| _ )_  _(_) |__| |   |   \\ ___ _ __| |___ _  _    |  \\/  |__ _ _ _  __ _ __ _ ___
| _ \\ || | | / _\` |_  | |) / -_) '_ \\ / _ \\ || |_  | |\\/| / _\` | ' \\/ _\` / _\` / -_)_
|___/\\_,_|_|_\\__,_(_) |___/\\___| .__/_\\___/\\_, (_) |_|  |_\\__,_|_||_\\__,_\\__, \\___(_)
                               |_|         |__/                          |___/`,

    `   _   _ _      _             _      _                        _
  /_\\ | | |  __| |___ _  _ __| |___ (_)_ _    __ _ _ _ _  _  | |__ _ _ _  __ _ _  _ __ _ __ _ ___
 / _ \\| | | / _| / _ \\ || / _\` (_-< | | ' \\  / _\` | ' \\ || | | / _\` | ' \\/ _\` | || / _\` / _\` / -_)_
/_/ \\_\\_|_| \\__|_\\___/\\_,_\\__,_/__/ |_|_||_| \\__,_|_||_\\_, | |_\\__,_|_||_\\__, |\\_,_\\__,_\\__, \\___(_)
                                                       |__/              |___/          |___/`,

    `__      ___         _                                    _          _          _             _           _          ___
\\ \\    / / |_  __ _| |_   __ _ _ _ ___  __ __ _____   __| |___ _ __| |___ _  _(_)_ _  __ _  | |_ ___  __| |__ _ _  |__ \\
 \\ \\/\\/ /| ' \\/ _\` |  _| / _\` | '_/ -_) \\ V  V / -_) / _\` / -_) '_ \\ / _ \\ || | | ' \\/ _\` | |  _/ _ \\/ _\` / _\` | || |/_/
  \\_/\\_/ |_||_\\__,_|\\__| \\__,_|_| \\___|  \\_/\\_/\\___| \\__,_\\___| .__/_\\___/\\_, |_|_||_\\__, |  \\__\\___/\\__,_\\__,_|\\_, (_)
                                                              |_|         |__/       |___/                      |__/`,
];

// Y = yellow (#f7bf2a), P = pink (#f26e7e), V = purple (#a855f7)
const cubeStyleCodes = "YPYVPYVPYVPVPVPVPVPVPVPVPVPV";

const S = "font-family:monospace;font-weight:bold;color:";
const styleMap: Record<string, string> = {
    Y: S + "#f7bf2a",
    P: S + "#f26e7e",
    V: S + "#a855f7",
};

// prettier-ignore
const cubeColorFormat = "%c             :+*###*+:             \n             +#######+             \n     .:-==-:  :-===-:  :-==-:.     \n    =#######*:       :*#######=    \n    .=*****+-   ...   -+*****=.    \n%c .--:        %c-+*###*+- %c        ::  \n%c =***+:      %c+#######+ %c     .-#@#: \n%c :+*+*+:   . %c .:---:.  %c    .=@@@=. \n%c  :=***-  =++=: %c     -++:  .+%%*-.  \n%c    .::   +*+**-%c   :+@@#:   ..     \n%c .==:     .+****:%c  .=@@#-      .::.\n%c =***+-     :=+=.%c  :=-.     .=%%@*:\n%c :+*++*:   ..   %c           .=@@%%-. \n%c  .=+**-  =**+- %c    .=**:  .+%%*:   \n%c    .:.   =*+**=%c   :*@@#:          \n%c          .=****:%c  .=@@*:\n%c            :==-%c   :=:             ";

const cubeColorStyles = cubeStyleCodes.split("").map((c: string) => styleMap[c]);

const linksText = [
    ["GitHub Repository", "https://github.com/pulumi/pulumi"],
    ["Careers", "https://pulumi.com/careers"],
    ["Docs", "https://pulumi.com/docs"],
    ["Slack", "https://slack.pulumi.com"],
]
    .map(([label, url]: string[]) => `- ${label}  ${url}`)
    .join("\n");

// Pick one random art: either the colored cube or one of the ASCII taglines
const allArts = [
    {
        format: cubeColorFormat + "\n\n%c" + linksText,
        styles: [...cubeColorStyles, S + "#f7bf2a"],
    },
    ...taglineArts.map((a) => ({
        format: `%c${a}\n\n%c` + linksText,
        styles: [S + "#8b5cf6", S + "#f7bf2a"],
    })),
];

const art = allArts[Math.floor(Math.random() * allArts.length)];
console.log(art.format, ...art.styles);
