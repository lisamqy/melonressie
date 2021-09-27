function Homepage() {
    return (
      <React.Fragment>
        <h4>
          Log in to make your melon tasting reservation today! <br />
          <a href="/new">Sign Up</a>
        </h4>
        <br />
        <form>
          <label htmlFor="login">
            Username:
            <input type="user" className="user" /> 
            <br />
            Email:
            <input type="email" className="email" />
          </label>
          <br /><br />
          <input type="submit" value="Submit" />
        </form>
  
      </React.Fragment>
    );
  }
  
  ReactDOM.render(<Homepage />, document.getElementById('app'));