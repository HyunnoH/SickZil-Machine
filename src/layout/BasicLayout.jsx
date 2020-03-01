import React from "react";
import { Navbar, Nav, NavItem } from "reactstrap";

const BasicLayout = content => {
  return (
    <div>
      <Navbar color="dark" fixed>
        <Nav>
          <NavItem>
            <button>
              <i>Text</i>
            </button>
          </NavItem>
          <NavItem>
            <button>
              <i>Text</i>
            </button>
          </NavItem>
          <NavItem>
            <button>
              <i>Text</i>
            </button>
          </NavItem>
          <NavItem>
            <button>
              <i>Text</i>
            </button>
          </NavItem>
        </Nav>
      </Navbar>
    </div>
  );
};

export default BasicLayout;
