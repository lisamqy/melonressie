function Reservation() {
    return (
      <React.Fragment>
        <h1>Create your reservation now 🍉</h1>
        
        <form action="/reservation" method="POST">
            <label htmlFor="datetime-select">
            Date:
            <input type="date" className="date" required />
            Start Time:
            <input type="time" className="start-time" step="1800" required  />
            </label>

            <input type="submit" value="Submit" />

        </form>
  
      </React.Fragment>
    );
  }
  
  ReactDOM.render(<Reservation />, document.getElementById('app'));