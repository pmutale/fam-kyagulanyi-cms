import ReactDOM from "react-dom";
import React from "react";
import { AppContainer } from "react-hot-loader";

import SiteUnderConstruction from "./components/index";

import "../less/main.less";
import "../scss/main.scss";

const Render = Component => {
	ReactDOM.render(
		<AppContainer>
			<Component/>
		</AppContainer>,
		document.getElementById("mwebaza")
	);
};

Render(SiteUnderConstruction);

if (module.hot) {
	module.hot.accept(SiteUnderConstruction, () => {
		const NextApp = require("./components/index.jsx").default;
		Render(<NextApp/>);
	})
}
