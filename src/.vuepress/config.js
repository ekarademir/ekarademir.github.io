module.exports = {
    title: 'Ertugrul Karademir',
    description: 'Personal Website',
    plugins: [
        '@vuepress/last-updated'
    ],
    themeConfig: {
        search: false,
        lastUpdated: 'Last Updated', // string | boolean
        nav: [
            {
                text: 'Home',
                link: '/'
            },
            {
                text: 'Projects',
                link: '/projects'
            },
            {
                text: 'CV',
                link: '/cv'
            },
            {
                text: 'GitHub',
                link: 'https://github.com/ekarademir'
            },
            {
                text: 'LinkedIn',
                link: 'https://www.linkedin.com/in/ekarademir/'
            },
        ]
    }
}
