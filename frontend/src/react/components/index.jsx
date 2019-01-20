import React from "react"
import { Message, Icon, Grid } from "semantic-ui-react"

export default class  SiteUnderConstruction extends React.Component {
  render() {
    console.log("i am not a dead man");
    return (
      <Grid textAlign="center" style={{height: "100%"}} verticalAlign="middle">
        <Grid.Column style={{maxWidth: 450}}>
          <Message icon>
            <Icon name="circle notched" loading/>
            <Message.Content>
              <Message.Header>Hi visitors</Message.Header>
                We are also  under alot of construction! Keep us tab for great features
            </Message.Content>
          </Message>
        </Grid.Column>
      </Grid>
    )
  }

}


