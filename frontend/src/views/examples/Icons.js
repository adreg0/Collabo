/*!

=========================================================
* Argon Dashboard React - v1.2.0
=========================================================

* Product Page: https://www.creative-tim.com/product/argon-dashboard-react
* Copyright 2021 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/argon-dashboard-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import React, { useState } from "react";
// react component that copies the given text inside your clipboard
import { CopyToClipboard } from "react-copy-to-clipboard";
import repos from "../../repos.json"
// reactstrap components
import {
  Card,
  CardHeader,
  CardBody,
  Container,
  Row,
  Col,
  UncontrolledTooltip,
} from "reactstrap";
// core components
import Header from "components/Headers/Header.js";

const Icons = () => {
  const [copiedText, setCopiedText] = useState();
  return (
    
    <>
      <Header />
      {/* Page content */}
      <Container className="mt--7" fluid>
        {/* Table */}
        <Row>
          <div className="col">
            <Card className="shadow">
              <CardHeader className="bg-transparent">
                <h3 className="mb-0">Repositories</h3>
              </CardHeader>
              <CardBody>
                <Row className="icon-examples">
                {repos.map((object, i) => 
                
                <Col lg="3" md="6">
                <button
                  className="btn-icon-clipboard"
                  type="button"
                  onClick={()=>{
                    window.open("https://github.com/amFOSS/"+object,"_blank").focus()
                  }}
                >
                  <div>
                    <i className="ni ni-active-40" />
                    <span>{object}</span>
                  </div>
                </button>
              
                </Col>
                
                )}
             
                
                </Row>
              </CardBody>
            </Card>
          </div>
        </Row>
      </Container>
    </>
  );
};

export default Icons;
