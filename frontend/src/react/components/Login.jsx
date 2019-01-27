import React from "react";
import { Button, Form, Grid, Header, Message, Segment, Icon } from "semantic-ui-react";
import Cookies from "js-cookie";

// import

class LoginForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      loginCreditials: {
        username: "",
        password: "",
      },
      loginErrors: {
        error: "",
        status: false
      }
    }
    this.onSubmit = this.onSubmit.bind(this)
    this.handleChange = this.handleChange.bind(this)
  }

  onSubmit () {
    fetch('/users/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': Cookies.get('csrftoken')
      },
      body: JSON.stringify(
        this.state.loginCreditials
      )
    })
      .then(response => response.json().then((data) => {
          const loginErrors = this.state.loginErrors;
          if (data.error) {
            loginErrors.error = data.error;
            loginErrors.status = true;
            this.setState({loginErrors})
          } else {
            loginErrors.error = null;
            loginErrors.status = false;
            this.setState(loginErrors)
          }
        })
      )
      .catch(error => console.error('Login Error', error))
  }

  handleChange(e, { name, value }) {
    const loginCreditials = this.state.loginCreditials;
    loginCreditials[name] = value;
    this.setState(loginCreditials)
  }

  render() {
    const { loginCreditials: { username, password }, loginErrors: { status, error } } = this.state
    const formStyle = {
      position: 'absolute',
      transform: 'translate(-50%, -50%)',
      left: '50%',
      top: '50%',
      width: '50%'
    }
    return (
      <div style={formStyle} className="login-form">
        <Grid centered>
          <Grid.Column>
            <Header as="h2" color="grey" textAlign="center">
              <Icon name="user"/> Log-in to your account
            </Header>
            {status ? <Message error header={'Action Forbidden'} content={error}/> : null}
            <Form size="large">
              {/*<Segment>*/}
                <Form.Input
                  value={username}
                  error={status}
                  fluid
                  onChange={this.handleChange}
                  icon="user"
                  name='username'
                  iconPosition="left"
                  placeholder="Username"/>
                <Form.Input
                  error={status}
                  fluid
                  onChange={this.handleChange}
                  value={password}
                  icon="lock"
                  name="password"
                  iconPosition="left"
                  placeholder="Password"
                  type="password"
                />

                <Button
                  positive
                  fluid
                  onClick={this.onSubmit}
                  size="large">
                  Login
                </Button>
              {/*</Segment>*/}
            </Form>
            <Message info>
              Are you part of the Family? <a href="#">Sign Up</a>
            </Message>
          </Grid.Column>
        </Grid>
      </div>
    );
  };
};

export default LoginForm
