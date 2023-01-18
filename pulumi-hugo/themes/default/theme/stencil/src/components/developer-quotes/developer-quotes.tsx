import { Component, Prop, h } from "@stencil/core";

@Component({
    tag: "pulumi-developer-quotes",
    styleUrl: "developer-quotes.scss",
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
                    return <i class="fas fa-envelope text-gray-500 text-xl"></i>
                case "blog":
                    return <i class="fas fa-blog text-gray-500 text-xl"></i>
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
            <div class="lg:flex flex-row block">
                {
                    quotes.map(col => {
                        return (
                            <div class="lg:w-6/12 w-12/12 mx-8"> 
                                {
                                    col.map(q => {
                                        return ( 
                                            <div class="quote-card my-8 p-2 rounded-lg max-w-80">
                                                <a class="flex flex-col" href={ this.enableLink(q.source) ? q.link : undefined } target="_blank" rel="noopener noreferrer">
                                                    <div class="w-full flex-grow text-justify p-3 text-gray-700">"{ q.message }"</div>
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
