
export class Host{
  id : number;
  hostName : string;
  addrIp : string;
  adrMac : string;
  interfaces : String[];
  nbPaquet : number;
}

interface Interf {
  id : number;
  state: string;
  addrIp: string;
}
