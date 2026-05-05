import { Component, Prop, h } from "@stencil/core";

@Component({
    tag: "pulumi-developer-quotes",
    shadow: false,
})

export class DeveloperQuotes {
    
    @Prop()
    quotes: string;

    addLogo(quote) {
        function getLogo () {
            switch(quote.source) {
                case "twitter":
                    return <img class="w-6" src="/logos/tech/twitter.svg"></img>
                case "reddit":
                    return <img class="w-6" src="/logos/tech/reddit.svg"></img>
                case "email":
                    return <svg xmlns="http://www.w3.org/2000/svg" class="ph-icon ph-icon--regular text-gray-500 text-xl" fill="currentColor" viewBox="0 0 256 256" aria-hidden="true" focusable="false"><path d="M224,48H32a8,8,0,0,0-8,8V192a16,16,0,0,0,16,16H216a16,16,0,0,0,16-16V56A8,8,0,0,0,224,48Zm-96,85.15L52.57,64H203.43ZM98.71,128,40,181.81V74.19Zm11.84,10.85,12,11.05a8,8,0,0,0,10.82,0l12-11.05,58,53.15H52.57ZM157.29,128,216,74.18V181.82Z"/></svg>
                case "blog":
                    return <svg xmlns="http://www.w3.org/2000/svg" class="ph-icon ph-icon--regular text-gray-500 text-xl" fill="currentColor" viewBox="0 0 256 256" aria-hidden="true" focusable="false"><path d="M216,40H40A16,16,0,0,0,24,56V200a16,16,0,0,0,16,16H216a16,16,0,0,0,16-16V56A16,16,0,0,0,216,40Zm0,160H40V56H216V200ZM184,96a8,8,0,0,1-8,8H80a8,8,0,0,1,0-16h96A8,8,0,0,1,184,96Zm0,32a8,8,0,0,1-8,8H80a8,8,0,0,1,0-16h96A8,8,0,0,1,184,128Zm0,32a8,8,0,0,1-8,8H80a8,8,0,0,1,0-16h96A8,8,0,0,1,184,160Z"/></svg>
                case "slack":
                    return <img class="w-6" src="/logos/tech/slack.svg"></img>
                case "linkedin":
                    return <img class="w-6" src="/logos/tech/linkedin.svg"></img>
                default:
                    return <a>{ quote.source }</a>
            }
        }
        return {
            ...quote,
            logo: getLogo(),
        }
    }

    enableLink(source: string) {
        // disable links for quotes coming from theses sources.
        const noLinks = [
            "slack",
            "email"
        ];
        return !noLinks.includes(source);
    }

    render() {
        let quotes = JSON.parse(this.quotes)
        // move featured quotes to the top.
        .sort((a,b) => {
            if (a.featured && b.featured) {
                return 0;
            }
            if (a.featured && !b.featured) {
                return -1;
            }
            if (!a.featured && b.featured) {
                return 1;
            }
        })
        // add logo based on type.
        .map(this.addLogo)
        // split into two columns.
        .reduce((prev, curr, i) => {
            if (i%2) {
                prev[1].push(curr)
            } else {
                prev[0].push(curr);
            }
            return prev;
        }, [[],[]]);

        return (
            <div class="container mx-auto">
                {
                    quotes.map(col => {
                        return (
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-4"> 
                                {
                                    col.map(q => {
                                        return ( 
                                            <div class="border border-gray-300 p-4 rounded-xl w-full">
                                                <a class="flex flex-col" href={ this.enableLink(q.source) ? q.link : undefined } target="_blank" rel="noopener noreferrer">
                                                    <div class="w-full flex-grow text-justify p-3 text-lg">"{ q.message }"</div>
                                                    <div class="flex flex-row">
                                                        <div class="p-3 text-gray-500">
                                                            { q.author }
                                                        </div>
                                                        <div class="flex-grow">
                                                        </div>
                                                        <div class="p-3">
                                                            { q.logo }
                                                        </div>
                                                    </div>
                                                </a>
                                            </div>
                                        )
                                    })
                                }
                            </div>
                        )
                    })
                }
            </div>
        )
    }
}
