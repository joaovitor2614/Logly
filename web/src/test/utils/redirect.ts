import { Router } from "vue-router";


export function verifyRedirect(buttonIDName: string, expectedRoutePath: string, router: Router) {
    cy.get(buttonIDName).click();
    cy.wrap(router.isReady()).then(() => {
        cy.wrap(router.currentRoute.value.fullPath).should('eq', expectedRoutePath)
    })
}




export const wellsDummyInfo = [
    {
        name: 'Well 1',
        _id: "sasdasdasdqwqw1221",
        create_time: '2022-01-01T00:00:00.000Z',
        company: 'Company 1',
        start: 2000,
        stop: 3000,
        welllogs: [
            {
                name: 'DEPTH',
                unit: "",
                _id: "jajsoj12112sajosa",
                create_time: '2022-01-01T00:00:00.000Z',
                description: 'Description 1',
                data: []
            },
            {
                name: 'GR',
                unit: "",
                _id: "jajsoj12112sajasasosa",
                create_time: '2022-01-01T00:00:00.000Z',
                description: 'Description 2',
                data: []
            },
        ]
    },
    {
        name: 'Well 2',
        _id: "sasdasdasdqwqw",
        company: 'Company 2',
        start: 2000,
        stop: 4000,
        create_time: '2022-01-01T00:00:00.000Z',
        welllogs: [
            {
                name: 'DEPTH',
                unit: "",
                _id: "jajsojsajo1221a",
                create_time: '2022-01-01T00:00:00.000Z',
                description: 'Description 1',
                data: []
            },
            {
                name: 'GR',
                unit: "",
                _id: "jajsojsajosa",
                create_time: '2022-01-01T00:00:00.000Z',
                description: 'Description 2',
                data: []
            },
            {
                name: 'RHOB',
                unit: "",
                create_time: '2022-01-01T00:00:00.000Z',
                description: 'Description 3',
                data: []
            }
        ]
    }
]

export const wellLogsDummyInfo = [
            {
                name: 'DEPTH',
                unit: "",
                _id: "jajsojsajo1221a",
                create_time: '2022-01-01T00:00:00.000Z',
                description: 'Description 1',
                data: []
            },
            {
                name: 'GR',
                unit: "",
                _id: "jajsojsajosa",
                create_time: '2022-01-01T00:00:00.000Z',
                description: 'Description 2',
                data: []
            },
            {
                name: 'RHOB',
                unit: "",
                create_time: '2022-01-01T00:00:00.000Z',
                description: 'Description 3',
                data: []
            }
]