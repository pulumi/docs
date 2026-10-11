import { Destination } from "./types";

export interface Category {
    key: string;
    name: string;
    description: string;
    tools: Destination[];
    toggleable: boolean;
}

const MARKETING_NAMES = ["HubSpot", "AWS S3", "Google Analytics 4 Web"];
const ADVERTISING_NAMES = ["LinkedIn Insight Tag", "Google Ads (Gtag)"];

export function categorizeDestinations(destinations: Destination[]): Category[] {
    const marketing: Destination[] = [];
    const advertising: Destination[] = [];
    const other: Destination[] = [];

    for (const dest of destinations) {
        if (MARKETING_NAMES.includes(dest.name)) {
            marketing.push(dest);
        } else if (ADVERTISING_NAMES.includes(dest.name)) {
            advertising.push(dest);
        } else {
            other.push(dest);
        }
    }

    const categories: Category[] = [];

    if (marketing.length > 0) {
        categories.push({
            key: "marketingAndAnalytics",
            name: "Marketing and Analytics",
            description:
                "To understand user behavior in order to provide you with a more relevant browsing experience or personalize the content on our site.",
            tools: marketing,
            toggleable: true,
        });
    }

    if (advertising.length > 0) {
        categories.push({
            key: "advertising",
            name: "Advertising",
            description:
                "To personalize and measure the effectiveness of advertising on our site and other websites.",
            tools: advertising,
            toggleable: true,
        });
    }

    if (other.length > 0) {
        categories.push({
            key: "other",
            name: "Other",
            description: "Other tools and integrations used on our site.",
            tools: other,
            toggleable: true,
        });
    }

    categories.push({
        key: "essential",
        name: "Essential",
        description:
            "We use browser cookies that are necessary for the site to work as intended. For example, we store your website data collection preferences so we can honor them if you return to our site. You can disable these cookies in your browser settings but if you do the site may not work as intended.",
        tools: [],
        toggleable: false,
    });

    return categories;
}
