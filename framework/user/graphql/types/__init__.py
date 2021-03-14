import graphene
from user.models import User

class UserBasicObj(
    graphene.ObjectType,
    description='the user type'
):
    id = graphene.ID() 
    email = graphene.email()
    phone = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    motives = graphene.String()
    tech = graphene.String()
    org_url = graphene.String()
    projects = graphene.String()
    status = graphene.String()
    city = graphene.String()

    
    def resolve_id(self, info):
        if isinstance(self, User):
            return self.id
    def resolve_email(self, info):
        if isinstance(self, User):
            return self.email
    def resolve_phoneNo(self, info):
        if isinstance(self, User):
            return self.phone
    def resolve_firstName(self, info):
        if isinstance(self, User):
            return self.first_name
    def resolve_lastName(self, info):
        if isinstance(self, User):
            return self.last_name
    def resolve_motives(self, info):
        if isinstance(self, User):
            return self.motives   
    def resolve_tech(self, info):
        if isinstance(self, User):
            return self.tech_stack  
    def resolve_org_url(self, info):
        if isinstance(self, User):
            return self.org_url   
    def resolve_projects(self, info):
        if isinstance(self, User):
            return self.projects
    def resolve_status(self, info):
        if isinstance(self, User):
            return self.status
    def resolve_city(self, info):
        if isinstance(self, User):
            return self.city