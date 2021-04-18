import graphene


# schema for a particular object
class Movies(graphene.ObjectType):
    title = graphene.String(required=True)
    stars = graphene.Int(required=True)



# query
class Query(graphene.ObjectType):
    Movie= graphene.Field(Movies,title=graphene.String())
    def resolve_Movie(root,info,title): 
        return Movies(title=title, stars=5 )


# mutation
class CreateMovie(graphene.Mutation):
    class Arguments:
        titles=graphene.String()
        star=graphene.Int()        
    
    ok=graphene.Boolean(required=True)
    Movietitle=graphene.String(required=True)

    def mutate(self,info,titles,star):
        ok=True
        Movietitle=titles
        return CreateMovie(ok=ok,Movietitle=Movietitle)



class Mutation(graphene.ObjectType):
    createMovie=CreateMovie.Field()


schema = graphene.Schema(query=Query,mutation=Mutation)


Queryresult=schema.execute('''
query test($name: String){
    Movie(title:$name){
        title,
        stars
    }
}
''',
variables={'name':'jedi'}
)


# print(Queryresult.data.items() )


MutateResult=schema.execute('''
mutation createUser{
    createMovie(titles:"skywalker",star:3){
        ok,
        Movietitle
    }
    
}

''',
)


print(MutateResult)