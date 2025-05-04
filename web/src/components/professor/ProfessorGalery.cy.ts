import { useProfessorStore } from "@/stores"
import ProfessorGalery from './ProfessorGalery.vue'



describe('<ProfessorGalery />', () => {
  it('renders', () => {
    const professorStore = useProfessorStore()
    professorStore.professorCollection.push({
        _id: '1',
        name: 'João Vitor',
        image: '',
        gender: 'male',
        comments: [],
        disciplines: [],
        upvotes: [],
        downvotes: [],
        phone: '21912912'
    })
    professorStore.professorCollection.push({
        _id: '2',
        name: 'Marina',
        image: '',
        gender: 'female',
        comments: [],
        disciplines: [],
        upvotes: [],
        downvotes: [],
        phone: '21912912'
    } as App.Professor.Professor)

    // see: https://on.cypress.io/mounting-vue
    cy.mountWithPiniaVuetify(ProfessorGalery)
    #cy.get('#test-professor-card').should('have.length', 2)


  })
})