function Reservation() {
    return (
      <React.Fragment>
        <h1>Create your reservation now 🍉</h1>
        
        <form>
          <label htmlFor="date-select">
            Date:
            <input type="date" className="date" />
            Start Time:
            <input type="time" className="start-time" />
          </label>
        </form>
  
      </React.Fragment>
    );
  }
  
  ReactDOM.render(<Homepage />, document.getElementById('app'));